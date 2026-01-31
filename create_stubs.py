#!/usr/bin/env python3
"""
Script to create stub files for missing concepts.
"""

import os

def create_stub_files(concept, subconcept):
    base_path = f"concepts/{concept}/{subconcept}"
    os.makedirs(base_path, exist_ok=True)

    # notes.md
    notes_content = f"# {subconcept.replace('_', ' ').title()}\n\n## Overview\n\nTODO: Add notes here.\n"
    with open(f"{base_path}/notes.md", "w") as f:
        f.write(notes_content)

    # examples.py
    examples_content = f"""def run():
    print("=== {subconcept.replace('_', ' ').title()} Examples ===\\n")

    # TODO: Add examples here

if __name__ == "__main__":
    run()
"""
    with open(f"{base_path}/examples.py", "w") as f:
        f.write(examples_content)

    # exercises.py
    exercises_content = f"""\"\"\"
{subconcept.replace('_', ' ').upper()} — EXERCISES

Instructions:
- TODO: Add instructions
\"\"\"

# TODO: Add exercises
"""
    with open(f"{base_path}/exercises.py", "w") as f:
        f.write(exercises_content)

    # solutions.py
    solutions_content = f"""\"\"\"
{subconcept.replace('_', ' ').upper()} — SOLUTIONS
\"\"\"

# TODO: Add solutions
"""
    with open(f"{base_path}/solutions.py", "w") as f:
        f.write(solutions_content)

# List of missing concepts and subconcepts
missing = {
    "advanced_language_features": ["13_memoization_patterns"],
    "iterators_data_flow": [
        "02_custom_iterators",
        "03_lazy_evaluation",
        "04_streaming_pipelines",
        "05_memory_efficient_iteration",
        "06_itertools_patterns",
        "07_advanced_comprehensions",
        "08_structural_pattern_matching"
    ],
    "threading_synchronization": [
        "02_thread_lifecycle",
        "03_locks",
        "04_reentrant_locks",
        "05_semaphores",
        "06_condition_variables",
        "07_deadlocks",
        "08_race_conditions",
        "09_thread_pools",
        "10_producer_consumer_queues"
    ],
    "gil_parallelism": [
        "03_io_bound_threading_benefits",
        "04_gil_workarounds",
        "05_workload_classification"
    ],
    "multiprocessing": [
        "03_pipes",
        "04_queues",
        "05_shared_memory",
        "06_fork_vs_spawn_modes",
        "07_pickle_serialization_costs",
        "08_interprocess_communication_patterns"
    ],
    "async_programming": [
        "02_async_await_syntax",
        "03_tasks",
        "04_futures",
        "05_async_context_managers",
        "06_async_iterators",
        "07_non_blocking_io",
        "08_structured_concurrency",
        "09_trio_concepts",
        "10_anyio_concepts"
    ],
    "testing_advanced": [
        "02_fixtures",
        "03_parameterized_tests",
        "04_property_based_testing",
        "05_mocking",
        "06_patching",
        "07_test_doubles",
        "08_contract_testing"
    ],
    "standard_library_deep_dive": [
        "02_contextlib_helpers",
        "03_inspect_module",
        "04_weak_references",
        "05_typing_module_advanced_usage",
        "06_pathlib_patterns",
        "07_concurrent_futures_executors",
        "08_advanced_logging_configuration"
    ],
    "static_typing_system": [
        "02_generics",
        "03_protocols",
        "04_typeddict",
        "05_paramspec",
        "06_typevar_constraints"
    ]
}

# Also, for threading_synchronization/01_threading_module, add the py files
missing["threading_synchronization"].insert(0, "01_threading_module")

if __name__ == "__main__":
    for concept, subs in missing.items():
        for sub in subs:
            print(f"Creating {concept}/{sub}")
            create_stub_files(concept, sub)