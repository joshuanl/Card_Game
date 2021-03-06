#ifndef CARD_H
#define CARD_H 

#include <string>

using namespace std;

class Card
{
public:
	Card(int id, string name);
	Card(const Card &other);
	~Card();

	string getName() const;
	int getID() const;
	void printCard() const;

private:
	string card_name;
	int card_ID;
};


#endif