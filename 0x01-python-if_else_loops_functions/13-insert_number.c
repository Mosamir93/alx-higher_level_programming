#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: head of the list
 *@number: integer to be added
 *Return: address of the new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node != NULL)
	{
		if (node->next == NULL || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
