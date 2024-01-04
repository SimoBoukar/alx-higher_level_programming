#include"lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: address of head pointer
 * @number: number to insert
 *
 * Return: inserted node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!node || new_node->n < node->n)
	{
		new_node->next = node;
		return (*head = new_node);
	}

	while (node)
	{
		if (!node->next || new_node->n < node->next->n)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
