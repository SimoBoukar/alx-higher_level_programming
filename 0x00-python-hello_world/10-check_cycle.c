#include"lists.h"

/**
 * check_cycle - check if list is cycable
 * @list: pointer to check list
 *
 * Return: 1 if cycable, 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *x = list, *y = list;

	if (!list)
		return (0);
	while (y && y->next)
	{
		x = x->next;
		y = y->next->next;
		if (x == y)
		return (1);
	}
	return (0);
}
