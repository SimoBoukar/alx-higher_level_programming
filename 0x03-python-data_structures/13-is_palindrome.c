#include"lists.h"

/**
 * is_palindrome - check if linked lists is palindrome
 * @head: head of list
 *
 * Return: 0 if not a palindrome
 * 1 if its a palindrome
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palind(head, *head));
}

/**
 * palind - fnct to know if is palindrome
 * @head: head list
 * @end: end of list
 *
*/

int palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
