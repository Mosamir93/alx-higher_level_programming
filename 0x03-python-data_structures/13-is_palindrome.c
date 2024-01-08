#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome or empty 0 if not
 */

int is_palindrome(listint_t **head)
{
	int len, i, j, k;
	listint_t *current, *f_half, *s_half, *sm_half;

	current = *head;
	if (head == NULL || *head == NULL)
		return (1);
	for (len = 0; current->next != NULL; len++)
	{
		current = current->next;
	}
	current = *head;
	f_half = *head;
	s_half = *head;
	k = (len + 1) / 2;

	for (i = 0; i <= k; i++)
	{
		s_half = s_half->next;
	}
	k = len / 2;
	for (i = 1; i <= len / 2; i++, k--)
	{
		sm_half = s_half;
		for (j = 1; j < k; j++)
		{
			sm_half = sm_half->next;
		}
		if (f_half->n != sm_half->n)
			return (0);

		f_half = f_half->next;
	}
	return (1);
}
