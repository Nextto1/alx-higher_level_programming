#include "lists.h"

/**
 * listint_rev - set to reverses a linked list
 * @head: first node of the list pointer
 *
 * Return:Is the first node in the new list pointer
 */
void listint_rev(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *recent = *head;
	listint_t *next = NULL;

	while (recent)
	{
		next = recent->next;
		recent->next = old;
		old = recent;
		recent = next;
	}

	*head = old;
}

/**
 * is_palindrome - It verifies if the list is a palindrome
 * @head: Is a pointer to the linked list
 *
 * Return: 1 if is true, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tempt = *head, *tap = NULL;

	if (*head == NULL || (*head)->next == NULL)
	return (1);

	while (1)
	{
	fast = fast->next->next;
	if (!fast)
	{
		tap = slow->next;
		break;
	}
	if (!fast->next)
	{
		tap = slow->next->next;
		break;
	}
	slow = slow->next;
	}

	listint_rev(&tap);

	while (tap && tempt)
	{
	if (tempt->n == tap->n)
	{
		tap = tap->next;
		tempt = tempt->next;
	}
	else
	return (0);
	}

	if (!tap)
	return (1);

	return (0);
}
