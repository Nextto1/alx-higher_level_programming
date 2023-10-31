#include "lists.h"

/**
 * insert_node - is to put in a number into the linked list
 * @head: That is the head of the list
 * @number: the number to keep in the new node
 * Return: new node pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *fast;
	listint_t *new_n;

	fast = *head;

	new_n = malloc(sizeof(listint_t));
	if (new_n == NULL)
		return (NULL);
	new_n->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_n->next = *head;
		*head = new_n;
		return (new_n);
	}

	while (fast->next != NULL)
	{
		if ((fast->next)->n >= number)
		{
			new_n->next = fast->next;
			fast->next = new_n;
			return (new_n);
		}
		fast = fast->next;
	}

	new_n->next = NULL;
	fast->next = new_n;
	return (new_n);
}
