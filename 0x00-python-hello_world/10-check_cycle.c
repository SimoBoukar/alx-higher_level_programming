#include"lists.h"

int check_cycle(listint_t *list)
{
	listint_t *prev = list, *nex = list;

	if (!list)
		return (0);
	while (nex && nex->next)
	{
		prev = perv->next;
		nex = nex->next->next;
		if (prev = nex)
			return (1);
	}
	return (0);
}
