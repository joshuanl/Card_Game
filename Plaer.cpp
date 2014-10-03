#include "Plaer.h"
#include <iostream>

using namespace std;


Player::Player(string username, string password, int age){
	this->username = username;
	this->password = password
	this->age = age;
	createProfile();
}//end of constructor 

Player::~Player(){
	delete [] decklist;
	delete [] record;
}//end of destructor;

void Player::createProfile(){
	cout << "Creating your profile..." << endl;
	cout << "Name: ";
	cin >> name;
	cout << "Email address: ";
	cin >> email;
	cout << "Age: ";
	cin >> age;
	cout << "Country: ";
	cin >> country;
	cout << endl << "Security Question..." << endl;
	cout << "Enter a secret question.  You will be asked this question in case you forgret your username or password.";
	cout << ">> ";
	cin >> secret_question;
	cout << "Next provide the answer for your question (case sensitive)." << endl;
	cout << ">> ";
	cin >> secret_question_answer;
	cout << endl << "Finished creating your profile!" << endl << endl;
}//end of creating profile
void Player::changeQuestion();
const string Player::getQuestion() const;
const string Player::getAnswer() const;
vector<Deck> Player::getDecklist() const;
stack<Record> Player::getRecord() const;
void Player::fixDeckMaxSize(const int newSize);
int Player::currentDecklistSize();
void Player::removeDeck(int pos);
void Player::addDeck(Deck deck);
