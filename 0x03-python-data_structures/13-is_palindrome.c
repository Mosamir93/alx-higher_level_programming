#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome or empty, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	reverse_list(&slow);

	while (slow != NULL)
	{
		if (slow->n != (*head)->n)
			return (0);

		slow = slow->next;
		*head = (*head)->next;
	}

	return (1);
}
