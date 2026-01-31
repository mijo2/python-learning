"""
ITERATORS DATA FLOW SUBITERATORS DATA FLOW — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""

# Exercise 1: Simple data pipeline
# TODO: Create a basic streaming pipeline with filter and map operations
def simple_pipeline():
    """Create a pipeline that filters even numbers and doubles them"""
    # TODO: Create a list of numbers
    # TODO: Use filter() to get even numbers
    # TODO: Use map() to double the numbers
    # TODO: Convert to list and return
    pass

# Exercise 2: Generator-based pipeline
# TODO: Create a memory-efficient pipeline using generators
def generator_pipeline():
    """Create a pipeline that processes large datasets efficiently"""
    # TODO: Create generator that yields numbers
    # TODO: Filter even numbers
    # TODO: Square the numbers
    # TODO: Return generator (not list)
    pass

# Exercise 3: Multi-stage pipeline
# TODO: Create a pipeline with multiple transformation stages
def multi_stage_pipeline(data):
    """Apply multiple transformations in sequence"""
    # TODO: Filter out negative numbers
    # TODO: Take square root of remaining numbers
    # TODO: Convert to integers
    # TODO: Filter numbers greater than 10
    # TODO: Return final result
    pass

# Exercise 4: Pipeline with error handling
# TODO: Create a robust pipeline that handles errors gracefully
def safe_pipeline(data):
    """Pipeline that handles various data types and errors"""
    # TODO: Handle non-numeric data gracefully
    # TODO: Skip invalid values rather than crashing
    # TODO: Apply transformations only to valid data
    # TODO: Return processed valid results
    pass

# Exercise 5: Streaming file processor
# TODO: Create a pipeline that processes file data in chunks
def file_processing_pipeline(filename):
    """Process a file line by line with streaming operations"""
    # TODO: Open file for reading
    # TODO: Process lines one by one
    # TODO: Filter lines containing specific words
    # TODO: Transform remaining lines
    # TODO: Yield processed lines
    pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     print("=== Streaming Pipelines Demo ===\n")
#
#     # Test simple pipeline
#     print("1. Simple Pipeline:")
#     result1 = simple_pipeline()
#     print(f"Result: {result1}")
#
#     # Test generator pipeline
#     print("\n2. Generator Pipeline:")
#     gen_result = generator_pipeline()
#     print(f"First 5 results: {list(gen_result)[:5]}")
#
#     # Test multi-stage pipeline
#     print("\n3. Multi-stage Pipeline:")
#     test_data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#     result3 = multi_stage_pipeline(test_data)
#     print(f"Input: {test_data}")
#     print(f"Result: {result3}")
#
#     # Test safe pipeline
#     print("\n4. Safe Pipeline:")
#     mixed_data = [4, "invalid", 9, None, 16, 25.5, 36]
#     result4 = safe_pipeline(mixed_data)
#     print(f"Input: {mixed_data}")
#     print(f"Safe result: {result4}")
#
#     # Test file processing (requires a test file)
#     print("\n5. File Processing Pipeline:")
#     # Create a simple test file
#     test_content = """This is line 1
# Another line with Python
# Just a regular line
# Python programming is fun
# End of file"""
#
#     with open("test_file.txt", "w") as f:
#         f.write(test_content)
#
#     lines_with_python = list(file_processing_pipeline("test_file.txt"))
#     print(f"Lines containing 'Python': {lines_with_python}")
#
#     # Clean up
#     import os
#     os.remove("test_file.txt")
