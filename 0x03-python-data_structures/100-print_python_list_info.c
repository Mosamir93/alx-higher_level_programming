#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, memory, index;
	PyObject *type;
	PyListObject *list;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

	list = (PyListObject *)p;
	size = PyList_Size(p);
	memory = list->allocated;

	printf("[*] Allocated = %ld\n", memory);

	for (index = 0; index < size; index++)
	{
		type = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, PyType(type)->tp_name);
	}
}
