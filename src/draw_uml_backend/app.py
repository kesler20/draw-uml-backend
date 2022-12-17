from diet.diet import Food, Meal
import os
import pandas as pd
# FastAPI imports
from fastapi import FastAPI, Body, UploadFile, Depends, BackgroundTasks, Response, status
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, StreamingResponse
from starlette.requests import Request
import json
import pickle
from src.draw_uml_backend.fast_prototyping.main import ClassBuilder
from src.draw_uml_backend.fast_prototyping.mainjs import JsClassBuilder
from src.draw_uml_backend.fast_prototyping.test_main import TestClassBuilder
from draw_uml_backend.protocol_database.database_client import DatabaseClient
from draw_uml_backend.protocol_database.database_interface import DatabaseInterface

'''
The application backend will take requrest from any client "see origins list set as *"
Nevertheless, the endpoint architecture will take the following form

/application-name/HTTP METHOD/custom

In the case of sofiaApi the custom topic will refer to the name of the Table 
of interest in lowercase
'''

# ---------------------------------------------------#
#                                                    #
#     INITIALIZE APPLICATION AND CONFIGURATIONS      #
#                                                    #
# ---------------------------------------------------#

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = DatabaseClient("my_routine.db")
db = DatabaseInterface(client)


@app.get("/", tags=["root"])
async def read_root():
    response = RedirectResponse(url='/docs')
    return response

# ----------------------------------- #
#                                     #
#         APPLICATIONS ENDPOINTS      #
#                                     #
# ------------------------------------#


#----------------- SOFIA DIET ---------------#

@app.post('/sofia-diet/food/CREATE')
async def handle_upload(food=Body(...)):
    try:
        food = json.loads(food.decode())
    except:
        print(type(food))

    # initialise food objects with base amount
    food = Food(food["name"], float(food["cost"]),
                float(food["protein"]), int(food["calories"]), "")

    df1 = pd.read_excel("food.xlsx")
    df2 = pd.DataFrame(data={"Name": [food.name], "Cost (£)": [food.cost],
                       "calories (g/amount)": [food.calories], "protein (g/amount)": [food.protein]})
    df3 = pd.concat([df1, df2])
    df3.to_excel("food.xlsx", index=False)

    print("food created successfully ✅")

    return {'response': 'okay'}


@app.get('/sofia-diet/food/READ')
async def read_foods():
    df1 = pd.read_excel("food.xlsx")
    df2 = pd.DataFrame(data={"name": df1["Name"], "cost": df1["Cost (£)"],
                       "calories": df1["calories (g/amount)"], "protein": df1["protein (g/amount)"]})
    print(df2)
    return df2.to_json()


@app.delete('/sofia-diet/food/DELETE')
async def delete_meals(mealID=Body(...)):
    df = pd.read_excel("food.xlsx")
    df.filter(items=list(filter(lambda item: item != None, [None if i == mealID else i for i,
              row in enumerate(df["Name"])])), axis=0).to_excel("food.xlsx", index=False)

    return {'response': 'okay'}


@app.post('/sofia-diet/meal/CREATE')
async def handle_meal_upload(meal=Body(...)):
    try:
        meal: 'list[dict]' = json.loads(meal.decode())
    except:
        print(type(meal))

    recipe = []  # a collection of foods
    for food in meal["recipe"]:
        if len(list(food.keys())) == 1:
            pass
        else:
            recipe.append(Food(food["name"], float(food["cost"]),
                               float(food["protein"]), float(food["calories"]), int(food["amount"])))
    meal = Meal(meal["mealName"], recipe)

    df1 = pd.read_excel("meals.xlsx")
    df2 = pd.DataFrame(data={"Name": [meal.name], "Cost (£)": [meal.total["cost"]],
                       "calories (g/amount)": [meal.total["calories"]], "protein (g/amount)": [meal.total["protein"]]})
    df3 = pd.concat([df1, df2])
    print(df3)
    df3.to_excel("meals.xlsx", index=False)

    print("meal created successfully ✅")

    return {'response': 'okay'}


@app.get('/sofia-diet/meal/READ')
async def handle_meal_upload():
    df1 = pd.read_excel("meals.xlsx")
    df2 = pd.DataFrame(data={"name": df1["Name"], "cost": df1["Cost (£)"],
                       "calories": df1["calories (g/amount)"], "protein": df1["protein (g/amount)"]})
    print(df2)
    return df2.to_json()


@app.delete('/sofia-diet/meal/DELETE')
async def delete_meals(mealID=Body(...)):
    df = pd.read_excel("meals.xlsx")
    df.filter(items=list(filter(lambda item: item != None, [None if i == mealID else i for i,
              row in enumerate(df["Name"])])), axis=0).to_excel("meals.xlsx", index=False)

    return {'response': 'okay'}


@app.post('/sofia-diet/diet/CREATE')
async def handle_diet_upload(diet=Body(...)):
    try:
        diet: 'list[dict]' = json.loads(diet.decode())
    except:
        print(type(diet))

    df1 = pd.read_excel("diet.xlsx")
    if len(df1["day"].values) >= 7:
        df1 = pd.DataFrame([])

    name = []
    cost = []
    calories = []
    protein = []
    amount = []
    for meal in diet["meals"]:
        name.append(meal["name"])
        cost.append(meal["cost"])
        calories.append(meal["calories"])
        protein.append(meal["protein"])
        amount.append(meal["amount"])
    df2 = pd.DataFrame(data={"day": [diet["weekDay"] for _ in name], "Name": name, "Cost (£)": cost, "Calories (g/amount)": calories,
                       "protein (g/amount)": protein, "amount (g)": amount})

    df3 = pd.concat([df1, df2])
    df3.to_excel("diet.xlsx", index=False)

    print(df3)
    return {'response': 'okay'}


@app.get('/sofia-diet/diet/READ')
async def get_diet_file():
    return FileResponse("diet.xlsx", media_type="application/msexcel", filename="diet.xlsx")

#----------------- DRAW-UML ----------------#


@app.post('/draw-uml/CREATE')
async def handle_create_diagram(diagram=Body(...)):
    try:
        diagram = json.loads(diagram.decode())
    except:
        print(type(diagram))

    meta_data = diagram[0]
    final_class = ""
    final_js_class = ""
    final_test_class = ""
    class_names = [object["data"]['objectName'] for object in meta_data]
    for object in meta_data:
        class_name = (object["data"]['objectName'], object["data"]['comment'])
        methods = []
        properties = []
        for method in object["data"]["gridTable"]:
            if method["signature"].find("()") == -1:
                properties.append((method["signature"], method["type"]))
            else:
                methods.append(
                    (method["signature"], method["comment"], method["type"]))

        # CREATING THE PYTHON FILE
        new_class = ClassBuilder(class_name, methods, properties)
        final_class += new_class.check_types(class_names)
        final_class += new_class.build_class_name()
        final_class += new_class.build_constructor_head()
        final_class += new_class.build_constructor_body()
        final_class += new_class.build_class_methods()

        # CREATING THE JAVASCRIPT FILE
        new_js_class = JsClassBuilder(class_name, methods, properties)
        final_js_class += new_js_class.build_class_name(
            class_name[0] == class_names[0])
        final_js_class += new_js_class.build_constructor_head()
        final_js_class += new_js_class.build_constructor_body()
        final_js_class += new_js_class.build_class_methods()

        with open('file.py', "w") as f:
            f.write(final_class)

        with open('file.js', 'w') as f:
            f.write(final_js_class)

        # CREATING THE PYTHON TEST FILE
        new_class = TestClassBuilder(class_name, methods, properties)

        if class_name[0] is class_names[0]:
            final_test_class += new_class.check_types(class_names)
            final_test_class += new_class.build_initial_import()

        final_test_class += new_class.build_class_name()
        final_test_class += new_class.build_constructor_head()
        final_test_class += new_class.build_constructor_body()
        final_test_class += new_class.build_class_methods()
        final_test_class += new_class.build_tearDown()

        if class_name[0] is class_names[-1]:
            final_test_class += new_class.build_main_function_call()

        with open('test_file.py', "w") as f:
            f.write(final_test_class)

    return {"response", "files create successfully ✅"}


@app.get('/draw-uml/python_file')
async def handle_get_python_file():
    print("get python file called")
    return FileResponse("file.py", media_type="text/x-python", filename="file.py")


@app.get('/draw-uml/python_test_file')
async def handle_get_python_test_file():
    print("get python test file called")
    return FileResponse("test_file.py", media_type="text/x-python", filename="test_file.py")


@app.get('/draw-uml/javascript_file')
async def handle_get_javascript_file():
    print("get javascript file called")
    return FileResponse("file.js", media_type="text/javascript", filename="file.js")

#-------------- SOFIA API----------------#


@app.get('/sofia-api/workout')
async def handle_get_javascript_file():
    column_names = ["id", "exercises_id", "session_id", "week_day"]
    main_df = convert_sql_table_to_df(column_names, db, "Workout")
    return main_df.to_json()


@app.get('/sofia-api/exercise')
async def handle_get_javascript_file():
    column_names = ["id", "reps", "sets", "weight", "name"]
    main_df = convert_sql_table_to_df(column_names, db, "Exercise")
    return main_df.to_json()


@app.get('/sofia-api/fitness')
async def handle_get_javascript_file():
    column_names = ["id", "session_id", "maintanace_calories",
                    "muscle_mass", "body_fat", "weight"]
    main_df = convert_sql_table_to_df(column_names, db, "Fitness")
    return main_df.to_json()
