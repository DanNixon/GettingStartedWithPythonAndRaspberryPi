input metauml;

outputformat := "svg";
outputtemplate := "Chapter04_Inheritance.svg";

beginfig(1);
    EClass.Object(iClassNameOnly)("object")()();

    Class.Function("Function")
        ()
        (
          "+evaluate()"
        );

    Class.BinaryOperation("BinaryOperation")
        (
          "-_left_operand",
          "-_right_operand"
        )
        (
          "+set_left_operand()",
          "+set_right_operand()"
        );

    Class.Addition("Addition")
        ()
        (
          "+evaluate()"
        );

    Class.Subtraction("Subtraction")
        ()
        (
          "+evaluate()"
        );

    leftToRight(20)(
        Function,
        BinaryOperation
        );

    Group.abstractClasses(
        Function,
        BinaryOperation
        );

    leftToRight(20)(
        Addition,
        Subtraction
        );

    Group.subClasses(
        Addition,
        Subtraction
        );

    topToBottom(20)(
        Object,
        abstractClasses,
        subClasses
        );

    drawObjects(
        Object,
        abstractClasses,
        subClasses
        );

    link(inheritance)(Function.n -- Object.s);
    link(inheritance)(BinaryOperation.n -- Object.s);

    link(inheritance)(Addition.n -- Function.s);
    link(inheritance)(Addition.n -- BinaryOperation.s);
    link(inheritance)(Subtraction.n -- Function.s);
    link(inheritance)(Subtraction.n -- BinaryOperation.s);

endfig;

end
