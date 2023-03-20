

```mermaid
classDiagram
   Commander <|-- object
   Commander : + command list[str]
   Commander : + void int
   Commander : + run() int
   Commander : + execute() list
```
        