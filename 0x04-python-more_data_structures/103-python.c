#include <Python.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to the python list
 */

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	int i;
	PyListObject *pp;

	pp = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);
	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
		if (strcmp(pp->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(pp->ob_item[i]);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: pointer to the python list
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size < 10 ? size : 9);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", size + 1 <= 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i <= size - 1)
			printf(" ");
	}
	printf("\n");
}
