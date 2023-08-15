#include <stdio.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Function print list information about Python
 * @p: Pointer of type PyObject
 *
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *lst = (PyListObject *)p;
	Py_ssize_t i;
	PyObject *element;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(lst));
	printf("[*] Allocated = %ld\n", lst->allocated);


	for (i = 0; i < Py_SIZE(lst); ++i )
	{
		PyObject *element =PyList_GGET_ITEM(lst, i);
		printf("Element %ld: %s\n", Py_TYPE(element)->tp_name);
	}
}
