#!/usr/bin/env python3
"""
Interactive CLI tool for learning Python concepts.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Define concepts and their sub-concepts
CONCEPTS = [
    ("list_comprehensions", None),  # Flat
    ("advanced_language_features", [f"{i:02d}_{name}" for i, name in enumerate([
        "closures", "late_binding_behavior", "function_decorators", "class_decorators",
        "parameterized_decorators", "generators", "generator_pipelines", "coroutines",
        "context_managers", "custom_context_managers", "functools_utilities", "partial_functions",
        "memoization_patterns"
    ], 1)]),
    ("iterators_data_flow", [f"{i:02d}_{name}" for i, name in enumerate([
        "iterator_protocol", "custom_iterators", "lazy_evaluation", "streaming_pipelines",
        "memory_efficient_iteration", "itertools_patterns", "advanced_comprehensions",
        "structural_pattern_matching"
    ], 1)]),
    ("oop", [f"{i:02d}_{name}" for i, name in enumerate([
        "basic_oop", "data_model_dunders", "operator_overloading", "abstract_base_classes",
        "protocols", "multiple_inheritance_mro", "mixins", "composition_vs_inheritance",
        "dataclasses_attrs", "immutability", "slots", "metaclasses", "init_subclass"
    ], 1)]),
    ("python_internals", [f"{i:02d}_{name}" for i, name in enumerate([
        "bytecode_model", "interpreter_execution_flow", "cpython_vs_pypy", "object_model",
        "memory_layout", "reference_counting", "garbage_collection", "mutability_rules",
        "object_interning", "descriptor_protocol", "attribute_lookup_chain",
        "import_system_internals", "module_caching", "monkey_patching_risks"
    ], 1)]),
    ("gil_parallelism", [f"{i:02d}_{name}" for i, name in enumerate([
        "gil_behavior", "cpu_bound_limits", "io_bound_threading_benefits",
        "gil_workarounds", "workload_classification"
    ], 1)]),
    ("multiprocessing", [f"{i:02d}_{name}" for i, name in enumerate([
        "multiprocessing_module", "process_pools", "pipes", "queues", "shared_memory",
        "fork_vs_spawn_modes", "pickle_serialization_costs", "interprocess_communication_patterns"
    ], 1)]),
    ("async_programming", [f"{i:02d}_{name}" for i, name in enumerate([
        "asyncio_event_loop", "async_await_syntax", "tasks", "futures",
        "async_context_managers", "async_iterators", "non_blocking_io",
        "structured_concurrency", "trio_concepts", "anyio_concepts"
    ], 1)]),
    ("testing_advanced", [f"{i:02d}_{name}" for i, name in enumerate([
        "pytest_features", "fixtures", "parameterized_tests", "property_based_testing",
        "mocking", "patching", "test_doubles", "contract_testing"
    ], 1)]),
    ("standard_library_deep_dive", [f"{i:02d}_{name}" for i, name in enumerate([
        "collections_advanced", "contextlib_helpers", "inspect_module", "weak_references",
        "typing_module_advanced_usage", "pathlib_patterns", "concurrent_futures_executors",
        "advanced_logging_configuration"
    ], 1)]),
    ("static_typing_system", [f"{i:02d}_{name}" for i, name in enumerate([
        "type_hints_deep_dive", "generics", "protocols", "typeddict",
        "paramspec", "typevar_constraints"
    ], 1)]),
    ("threading_synchronization", [f"{i:02d}_{name}" for i, name in enumerate([
        "threading_module", "thread_lifecycle", "locks", "reentrant_locks",
        "semaphores", "condition_variables", "deadlocks", "race_conditions",
        "thread_pools", "producer_consumer_queues"
    ], 1)])
]

PROGRESS_FILE = "progress_tracker.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def get_path(concept, subconcept, file_type):
    if subconcept:
        if file_type == 'notes':
            return f"concepts/{concept}/{subconcept}/notes.md"
        else:
            return f"concepts/{concept}/{subconcept}/{file_type}.py"
    else:
        if file_type == 'notes':
            return f"concepts/{concept}/notes.py"
        else:
            return f"concepts/{concept}/{file_type}.py"

def run_tests(concept, subconcept):
    test_path = f"tests/test_{concept}_{subconcept if subconcept else 'main'}.py"
    if not os.path.exists(test_path):
        print(f"No tests found for {concept}/{subconcept}")
        return False

    result = subprocess.run([sys.executable, "-m", "pytest", test_path, "-v"], capture_output=True, text=True)
    print("Test Output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    return result.returncode == 0

def learning_session(concept, subconcepts):
    progress = load_progress()
    if concept not in progress:
        progress[concept] = {}

    for sub in subconcepts:
        if sub not in progress[concept]:
            progress[concept][sub] = {"notes": False, "examples": False, "exercises": False, "completed": False}

        sub_progress = progress[concept][sub]

        # Notes
        if not sub_progress["notes"]:
            notes_path = get_path(concept, sub, 'notes')
            print(f"\nRead the notes: {notes_path}")
            while input("Have you read the notes? (y/n): ").lower() != 'y':
                pass
            sub_progress["notes"] = True
            save_progress(progress)

        # Examples
        if not sub_progress["examples"]:
            examples_path = get_path(concept, sub, 'examples')
            print(f"\nCheck the examples: {examples_path}")
            while input("Have you checked the examples? (y/n): ").lower() != 'y':
                pass
            sub_progress["examples"] = True
            save_progress(progress)

        # Exercises
        if not sub_progress["exercises"]:
            exercises_path = get_path(concept, sub, 'exercises')
            print(f"\nImplement the exercises: {exercises_path}")
            while input("Have you implemented the exercises? (y/n): ").lower() != 'y':
                pass
            sub_progress["exercises"] = True
            save_progress(progress)

        # Run tests
        if not sub_progress["completed"]:
            print(f"\nRunning tests for {concept}/{sub}...")
            if run_tests(concept, sub):
                print("Tests passed!")
                sub_progress["completed"] = True
                save_progress(progress)

                # Offer to show solution
                show_solution = input("Would you like to see the solution? (y/n): ").lower() == 'y'
                if show_solution:
                    solutions_path = get_path(concept, sub, 'solutions')
                    print(f"Solution path: {solutions_path}")
                    input("Press Enter when ready to continue...")
            else:
                print("Tests failed. Please check your implementation.")
                continue

def main():
    print("Welcome to Python Learning CLI!")
    print("\nAvailable concepts:")

    for i, (concept, _) in enumerate(CONCEPTS, 1):
        print(f"{i}. {concept.replace('_', ' ').title()}")

    while True:
        try:
            choice = int(input("\nChoose a concept to start learning from (1-12): "))
            if 1 <= choice <= len(CONCEPTS):
                break
            print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    concept, subconcepts = CONCEPTS[choice - 1]

    if subconcepts is None:
        # Flat concept
        learning_session(concept, [None])
    else:
        # Nested concept
        learning_session(concept, subconcepts)

    print(f"\nCompleted learning session for {concept}!")

if __name__ == "__main__":
    main()
