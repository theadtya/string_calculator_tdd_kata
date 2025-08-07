class StringCalculator:
    def add(self, numbers: str) -> int:
        """Add method that takes a string of numbers and returns their sum"""
        if not numbers:
            return 0
        return sum(int(num) for num in numbers.split(","))
    
    