#include "lists.h"

/**
 *chech_cycle - checks if a singly linked list has a cycle in it or not
 *@list: the list's pointer
 *Return: 1 if there is a cycle 0 if there is not
 */

int check_cycle(listint_t *list)
{
	listint_t *ones = list, *twos = list;

	while (twos && twos->next)
	{
		ones = ones->next;
		twos = twos->next->next;
		if (ones == twos)
			return (1);
	}
	return (0);
}
