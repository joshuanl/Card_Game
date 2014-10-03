#ifndef PLAYER_H
#define PLAYER_H 

#include "Deck.h"
#include "Record.h"
#include <stack>
#include <string>

using namespace std;

class Player
{
public:
	Player(string username, string password, int age);
	~Player();
	void changeQuestion();
	const string getQuestion() const;
	const string getAnswer() const;
	vector<Deck> getDecklist() const;
	stack<Record> getRecord() const;
	void changeDeckListSize(const int newSize);
	int currentDecklistSize();
	void removeDeck(int pos);
	void addDeck(Deck deck);
	void createProfile();

private:
	string username;
	string password;
	string secret_question;
	string secret_question_answer;
	int age;
	string country;
	string name;
	string email;
	vector<Deck> decklist;
	stack<Record> Record;
	int decklist_max_size;
	int decklist_current_size;
};

#endif