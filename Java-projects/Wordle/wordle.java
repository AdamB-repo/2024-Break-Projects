import java.util.ArrayList; //We will store the words from words.txt in an array list
import java.util.*; //need collections for randomization using shuffle 
import java.io.File; //going to be reading words.txt so need this
import java.io.FileNotFoundException; //Just incase someone deletes words.txt, I will try and catch it
import java.util.Scanner; //Need this to read the words.txt file

public class wordle{

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

    public void displayGame(ArrayList<String> guesses){
        for (int i = 0; i < guesses.size(); i++){
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

        //Remember to remove these
        ArrayList<String> temp = new ArrayList<String>();
        temp.add("hi");
        temp.add("This");
        temp.add("is");
        temp.add("working");
        game.displayGame(temp);
    }
}