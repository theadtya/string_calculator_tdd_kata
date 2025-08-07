class StringCalculator:
    def add(self, numbers: str) -> int:
        """Add method that takes a string of numbers and returns their sum"""
        if not numbers:
            return 0
        
        # Check if custom delimiter is specified
        if numbers.startswith("//"):
            # Find the delimiter and numbers part
            delimiter_end = numbers.find("\n")
            if delimiter_end == -1:
                raise ValueError("Invalid custom delimiter format")
            
            delimiter = numbers[2:delimiter_end]
            numbers = numbers[delimiter_end + 1:]
        else:
            # Use default delimiters (comma and newline)
            delimiter = ","
            # Replace newlines with commas for backward compatibility
            numbers = numbers.replace("\n", ",")
        
        return sum(int(num) for num in numbers.split(delimiter))
    
    