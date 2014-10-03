#ifndef DECK_H
#define DECK_H 

#include <string>
#include <vector>
#include "Card.h"

using namespace std;

class Deck
{
public:
	Deck();
	~Deck();

	void shuffle();
	Card draw() const;
	void next();
	void first();
	int size() const;
	int sizeInGame() const;


private:
	string cardBack;
	string deck_name;
	int index;
	int size;
	int size_in_game;
	vector<Card> deck_of_cards;


};
#endif