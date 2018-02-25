#include <Python.h>
#include <utmpx.h>

static PyObject *users(PyObject *self, PyObject *args) {
	struct utmpx *utx;
	PyObject *py_username = NULL;
	PyObject *py_tty = NULL;
	PyObject *py_hostname = NULL;
	PyObject *py_tuple = NULL;
	PyObject *py_retlist = PyList_New(0);

	if (py_retlist == NULL)
		return NULL;
	while ((utx = getutxent()) != NULL) {
		if (utx->ut_type != USER_PROCESS)
			continue;
		py_username = PyUnicode_DecodeFSDefault(utx->ut_user);
		py_tty = PyUnicode_DecodeFSDefault(utx->ut_line);
		py_hostname = PyUnicode_DecodeFSDefault(utx->ut_host);
		py_tuple = Py_BuildValue(
			"(OOOfi)",
			py_username, // username
			py_tty, // tty
			py_hostname, // hostname
			(float)utx->ut_tv.tv_sec, // start time
			utx->ut_pid // process id
		);
		PyList_Append(py_retlist, py_tuple);
		Py_DECREF(py_username);
		Py_DECREF(py_tty);
		Py_DECREF(py_hostname);
		Py_DECREF(py_tuple);
	}
	endutxent();
	return py_retlist;
}

static PyMethodDef UsersMethods[] = {
    {"users", users, METH_VARARGS,
     "Return users as a list of tuples"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef usersmodule = {
    PyModuleDef_HEAD_INIT,
    "users",
    0,
    -1,
    UsersMethods
};


PyMODINIT_FUNC
PyInit_users(void)
{
	return PyModule_Create(&usersmodule);
}
