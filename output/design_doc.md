

```mermaid
classDiagram
   Student <|-- object
   Student : + name str
   Student : + age int
   Student : + class_room ClassRoom
```
        

```mermaid
classDiagram
   ClassRoom <|-- object
   ClassRoom : + subect str
```
        