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
	if (!head || !(*head))
		return (1);
	for (len = 0; current->next != NULL; len++)
	{
		current = current->next;
	}

	current = *head;
	f_half = *head;
	s_half = *head;
	sm_half = *head;
	k = len / 2;
	if (len % 2 != 0)
		k += 1;

	for (i = 1; i <= k; i++)
	{
		sm_half = sm_half->next;
		s_half = s_half->next;
	}
    k = len / 2;
	for (i = 1; i <= len / 2; i++)
	{
		for (j = 1; j < k; j++)
		{
			sm_half = sm_half->next;
		}
		if (f_half->n != sm_half->n)
			return (0);

		f_half = f_half->next;
		sm_half = s_half;
		k--;
	}
	return (1);
}
