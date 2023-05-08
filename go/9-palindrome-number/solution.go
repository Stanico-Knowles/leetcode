/* 
	Given an integer x, return true if x is a palindrome, and false otherwise.
	
	Follow up: Could you solve it without converting the integer to a string?
*/

func isPalindrome(x int) bool {   
	num := x 
    reversed := 0

    for num > 0 {
        lastDigit := num % 10
        reversed = 10 * reversed + lastDigit
        num = num / 10
    }

	return (x == reversed && x >= 0)
}