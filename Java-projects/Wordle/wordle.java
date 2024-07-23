//We will store the words from words.txt in an array list
//Need this to read the words.txt file
import java.util.*; //need collections for randomization using shuffle 
import java.io.File; //going to be reading words.txt so need this
import java.io.FileNotFoundException; //Just incase someone deletes words.txt, I will try and catch it

public class wordle{

    public static final String resetColour = "\u001B[0m";
    public static final String yellow = "\u001B[33m";
    public static final String green = "\u001B[32m";

    public ArrayList<String> getWords(){ //This method reads words.txt and extracts each of the words between the commas
        ArrayList<String> words = new ArrayList<String>(); //make the array for the words in words.txt
        try {
            File wordFile = new File("C:/Users/ajbro/OneDrive/Documents/2024-Break-Projects/Java-projects/Wordle/words.txt"); //This will work for me but you will need to specify your path to "words.txt"
            Scanner readWords = new Scanner(wordFile); 
            while (readWords.hasNextLine()){
                String wordData = readWords.nextLine(); //get the line from the word file
                String tempWord = new String(); //This will be used in the following code that will read from the lines extracted
                for (int i = 0; i < wordData.length(); i++){ //Add characters to tempWord from the lines until a comma is seen, then add the tempWord to the array and empty tempWord
                    if (wordData.charAt(i) == ','){
                        System.out.println(tempWord);
                        words.add(tempWord);
                        tempWord = "";
                    }
                    else{
                        tempWord += wordData.charAt(i);
                    }
                }
                System.out.println(tempWord); 
                words.add(tempWord); //need to add the final word as it won't have a comma after it
            }
            readWords.close();
        }
        catch (FileNotFoundException error){ //If words.txt doesn't exist, throw and error message to help the player understand what went wrong
            System.out.println("ERROR: words.txt not found, cannot play the game");
        }
        return(words);
    }

    public String chooseRandomWord(ArrayList<String> words){ //This method will randomly choose a word from the previous array to use in the game
        String chosenWord = new String(); //string where we will store the word
        Collections.shuffle(words); //Shuffle the list so we can randomly choose a word
        chosenWord = words.get(0); //Since we shuffled, the first word is random
        return chosenWord; //return the random word
    }

    public ArrayList<String> makeBaseGuessesArray(String chosenWord){ //This hides the word with '-' characters then returns the base gameboard for the user
        String hiddenWord = new String(); //will be used to hide the word
        ArrayList<String> gameDisplay = new ArrayList<String>(); //will be used to keep the guesses so the player can use prior guesses for future refernce
        for (int i = 0; i < chosenWord.length(); i++){ //loop to make a string to hide the word
            hiddenWord += '-';
        }
        for (int i = 0; i < 6; i++){ //loop to add the newly hidden word to an array
            gameDisplay.add(hiddenWord);
        }
        return gameDisplay;
    }

    public ArrayList<String> updateGameboard(ArrayList<String> gameboard, String guess, int index){
        gameboard.set(index, guess);
        return gameboard;
    }

    public String updateCharacterColours(String guess, String hiddenWord){
        String finalGuess = new String();
        for (int i = 0; i < guess.length(); i++){
            if (hiddenWord.length() > i){
                if (guess.charAt(i) == hiddenWord.charAt(i)){
                    finalGuess += green + guess.charAt(i) + resetColour;
                }
                else if (hiddenWord.indexOf(guess.charAt(i)) != -1){
                    finalGuess += yellow + guess.charAt(i) + resetColour;
                }
                else{
                    finalGuess += guess.charAt(i);
                }
            }
            else {
                if (hiddenWord.indexOf(guess.charAt(i)) != -1){
                    finalGuess += yellow + guess.charAt(i) + resetColour;
                }
                else{
                    finalGuess += guess.charAt(i);
                }
            }
        }
        return finalGuess;
    }

    public void displayGame(ArrayList<String> guesses){ //This will be used to allow the player to see the state of the game
        for (int i = 0; i < guesses.size(); i++){ //for each guess the player can make, this sets up the a string to print
            String setupString = "Guess ";
            setupString += Integer.toString(i);
            setupString += ": ";
            setupString += guesses.get(i);
            System.out.println(setupString);
        }
    }

    public static void main(String[] args){
        wordle game = new wordle();
        ArrayList<String> wordList = game.getWords();
        String hiddenWord = game.chooseRandomWord(wordList);
        System.out.println(hiddenWord);
        ArrayList<String> gameboard = game.makeBaseGuessesArray(hiddenWord);

        System.out.println("Hi, welcome to Wordle");

        Scanner gameScanner = new Scanner(System.in);

        for (int i = 0; i < 6; i++){
            game.displayGame(gameboard);
            System.out.println("Please guess the word");
            String guess = gameScanner.nextLine();
            if (guess.equals(hiddenWord)){
                System.out.println("\n");
                System.out.println("Woop woop, the word was '" + hiddenWord + "'");
                guess = green + guess + resetColour;
                game.updateGameboard(gameboard, guess, i);
                break;
            }
            else{
                System.out.println("\n");
                guess = game.updateCharacterColours(guess, hiddenWord);
                game.updateGameboard(gameboard, guess, i);
            }
        }

        gameScanner.close();
        game.displayGame(gameboard);
    }
}