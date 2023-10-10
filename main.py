#!/usr/bin/env python3
import json

def stable_marriage(men_set : dict, women_set: dict) -> dict:
	
	couples_man_side = { man : None for man in men_set }
	couples_woman_side = { woman : None for woman in women_set }

	while None in couples_man_side.values():
		for candidate in men_set.keys():
			index = 0
			while couples_man_side[candidate] is None:
				candidate_woman = men_set[candidate][index]

				if couples_woman_side[candidate_woman] is None:
					couples_man_side[candidate] = candidate_woman
					couples_woman_side[candidate_woman] = candidate

				else:
					current_husband = couples_woman_side[candidate_woman]
					if women_set[candidate_woman].index(candidate) < women_set[candidate_woman].index(current_husband):
						couples_man_side[candidate] = candidate_woman
						couples_woman_side[candidate_woman] = candidate
						couples_man_side[current_husband] = None
					else:
						index += 1
	return couples_man_side


if __name__ == '__main__':
	with open("./data/set_one.json", "r") as source:
		data = json.loads(source.read())
		result_set = stable_marriage(data["men"], data["women"])
		print('[+] Results')
		print(json.dumps(result_set, indent=2))