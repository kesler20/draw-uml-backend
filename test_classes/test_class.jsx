// library imports
import CustomButton from "./CustomButton";
import { ArrowCircleRightIcon } from "@heroicons/react/solid";
import { useState, useEffect } from "react";
import MQTTApi from "../apis/MQTTApi";

const Form = () => {
  const [command, setCommand] = useState("");
  const [clientCommand, setClientCommand] = useState("");

  useEffect(() => {
    const form = document.querySelector("input");
    form.focus();
    return () => {
      form.removeEventListener("focus", () => {});
    };
  }, []);

  useEffect(() => {
    if (clientCommand !== "") {
      postCommand(command);
      console.log("command posted");
    }
  }, [clientCommand]);

  useEffect(() => {
    if (clientCommand !== "") {
      const topic = "sofia-silent";
      const clientID = "sofia-silent-mqtt-client";

      const mqttApi = new MQTTApi(clientID);

      // connect client to ws
      mqttApi.onConnect(() => {
        // subscribe to the topic
        mqttApi.subscribeClient(topic, () => {
          console.log("connected to sofia-silent");
        });

        // log any messages
        mqttApi.onMessage((msg) => {
          console.log(msg);
        });

        // publish new commands when the command state is updated
        mqttApi.publishMessage(topic, command);
        console.log(`${clientID} publish ${command}`);
      }, []);

      // unsubscribe the client when the component unmounts
      return mqttApi.unsubscribeClient(topic);
    }
  }, [clientCommand]);

  /**
   * this is a function called when the clientCommand state changes
   * @param {*} command - this is a string containing a command to sent to the sofia silent backend
   */
  const postCommand = async (command) => {
    const response = await fetch(`${process.env.REACT_APP_BACKEND_URL_DEV}`, {
      method: "POST",
      body: JSON.stringify(`${command}`),
    });
    response
      .then((res) => {
        return res.json((res) => {
          if (res.ok) {
            console.log(res);
          }
        });
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <>
      <h1 className="text-3xl sm:text-6xl font-bold text-center">
        What should I do?
      </h1>
      <form
        className="flex ring-4 rounded-md ring-slate-200  dark:ring-slate-800 focus-within:ring-teal-600 focus-within:ring-offset-4 bg-slate-200 ring-offset-slate-200 dark:ring-offset-slate-800"
        onSubmit={(e) => e.preventDefault()}
      >
        <input
          type="text"
          className="bg-inherit rounded-md font-sans text-slate-800  py-2 px-6 focus:outline-none text-xl sm:text-2xl placeholder:text-slate-400 caret-teal-600 appearance-none w-full"
          placeholder="Enter Command"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          autoFocus
          maxLength="64"
        />
        <button
          className="bg-inherit rounded-md font-sans text-slate-800  py-2 pr-6 focus:outline-none focus:text-teal-600 hover:text-teal-600"
          onClick={() => setClientCommand(command)}
        >
          <ArrowCircleRightIcon className="h-12 w-12 pointer-events-none" />
        </button>
      </form>

      <CustomButton text="Send Command" />
    </>
  );
};

export default Form;