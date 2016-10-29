open CInterface;

(*
exception Foreign of string
val load_lib : string -> dylib
val load_sym : dylib -> string -> sym
val get_sym : string -> string -> sym
*)

val pylib = load_lib "/opt/local/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/config-3.5m/libpython3.5m.dylib";
val Py_Initialize = call0 (load_sym pylib "Py_Initialize") () VOID;
fun PyRun_SimpleString s = call1 (load_sym pylib "PyRun_SimpleString") STRING INT s;
fun PyRun_SimpleFile s = call1 (load_sym pylib "PyRun_SimpleFile") STRING s;
fun Py_IsInitialized s = call1 (load_sym pylib "Py_IsInitialized") VOID INT s;
Py_Initialize();
Py_IsInitialized();
PyRun_SimpleString "print (1*2*3)";