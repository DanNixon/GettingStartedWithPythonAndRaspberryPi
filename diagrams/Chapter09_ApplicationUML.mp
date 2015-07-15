input metauml;

outputformat := "svg";
outputtemplate := "Chapter09_ApplicationUML.svg";

beginfig(1);
    Class.CLI("unitconverter.CLI")
        ()
        (
        "+run_cli(): void",
        "+run_conversion(): void",
        "+run_list_units() :void"
        );

    Class.Converter("unitconverter.Converter")
        ()
        (
        "+get_table(name): UnitTable",
        "+get_conversions(): list"
        );

    Class.UnitTable("unitconverter.UnitTable")
        (
        "+base_unit: str",
        "+to_base_unit: dict",
        "+from_base_unit: dict"
        )
        (
        "+can_convert(): bool",
        "+convert(): dict"
        );

    EClass.Angle(iClassNameOnly)("angle")()();
    EClass.Energy(iClassNameOnly)("energy")()();
    EClass.Length(iClassNameOnly)("length")()();
    EClass.Mass(iClassNameOnly)("mass")()();
    EClass.Speed(iClassNameOnly)("speed")()();
    EClass.Temperature(iClassNameOnly)("temperature")()();
    EClass.Time(iClassNameOnly)("time")()();


    Package.unit_tables("unitconverter.unit_tables")(
        Angle,
        Energy,
        Length,
        Mass,
        Speed,
        Temperature,
        Time
    );

    Package.unitconverter("unitconverter")(
        CLI,
        Converter,
        UnitTable
    );


    leftToRight(20)(
        CLI,
        Converter,
        UnitTable
    );

    leftToRight(20)(
        Angle,
        Energy,
        Length,
        Mass,
        Speed,
        Temperature,
        Time
    );

    topToBottom(30)(
        unitconverter,
        unit_tables
    );


    drawObjects(
        unitconverter,
        unit_tables,
        CLI,
        Converter,
        UnitTable,
        Angle,
        Energy,
        Length,
        Mass,
        Speed,
        Temperature,
        Time
    );


    link(inheritance)(Angle.n -- UnitTable.s);
    link(inheritance)(Energy.n -- UnitTable.s);
    link(inheritance)(Length.n -- UnitTable.s);
    link(inheritance)(Mass.n -- UnitTable.s);
    link(inheritance)(Speed.n -- UnitTable.s);
    link(inheritance)(Temperature.n -- UnitTable.s);
    link(inheritance)(Time.n -- UnitTable.s);


endfig;

end
