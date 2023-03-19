

```mermaid
classDiagram
   Computer <|-- object
   Computer : + memory int
   Computer : + run list[str]
   Computer : - foll int
   Computer : + execute() str
   Computer : + foo() list
```
        