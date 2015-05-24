input metauml;

outputformat := "svg";
outputtemplate := "Chapter04_OOP.svg";

beginfig(1);
    EClass.Object(iClassNameOnly)("object")()();

    Class.Calculator("Calculator")
        (
          "-_input_list: list",
          "-_result: float"
        )
        (
          "+enter_value",
          "+enter_operation",
          "+evaluate",
          "+get_result",
          "+all_clear"
        );

    Class.Operation("Operation")
        (
          "-_operation: str"
        )
        (
          "+evaluate"
        );

    leftToRight(20)(
        Calculator,
        Operation
        );

    Group.subclasses(
        Calculator,
        Operation
        );

    topToBottom(20)(
        Object,
        subclasses
        );

    drawObjects(
        Object,
        subclasses
        );

    link(inheritance)(Calculator.n -- Object.s);
    link(inheritance)(Operation.n -- Object.s);

endfig;

end
