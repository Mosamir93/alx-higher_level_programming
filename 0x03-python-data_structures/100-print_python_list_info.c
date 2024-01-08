#include "python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the python list
 */

void print_python_list_info(PyObject *p)
{
	int size, memory, index;
	PyObject *type;

	size = PY_SIZE(p);
	memory = (PyListObject *)p->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", memory);

	for (index = 0; index < size; index++)
	{
		type = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, PyTYPE(type)->tp_name);
	}
}
