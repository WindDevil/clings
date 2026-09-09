cmake_minimum_required(VERSION 3.20)

project(
  clings
  VERSION 0.1.0
  DESCRIPTION "Hands-on exercises for learning the complete C language"
  LANGUAGES C
)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

find_package(Python3 COMPONENTS Interpreter REQUIRED)
find_package(Threads REQUIRED)

enable_testing()

add_library(clings_harness INTERFACE)
target_include_directories(
  clings_harness
  INTERFACE "${CMAKE_CURRENT_SOURCE_DIR}/include"
)
target_compile_definitions(
  clings_harness
  INTERFACE _POSIX_C_SOURCE=200809L _DEFAULT_SOURCE
)

if(CMAKE_C_COMPILER_ID MATCHES "GNU|Clang")
  target_compile_options(
    clings_harness
    INTERFACE
      -Wall
      -Wextra
      -Wpedantic
      -Werror
      -Wshadow
      -Wstrict-prototypes
      -Wpointer-arith
      -Wformat=2
      -Wundef
  )
endif()

function(clings_add_target target)
  add_executable(${target} ${ARGN})
  target_link_libraries(${target} PRIVATE clings_harness Threads::Threads)
  if(UNIX)
    target_link_libraries(${target} PRIVATE m)
  endif()
endfunction()

# Solutions are part of the default build and are registered with CTest.
file(GLOB_RECURSE clings_solution_sources
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/solutions"
  "${CMAKE_CURRENT_SOURCE_DIR}/solutions/*.c"
)
foreach(source IN LISTS clings_solution_sources)
  string(REPLACE "/" "_" target "solution_${source}")
  string(REPLACE ".c" "" target "${target}")
  clings_add_target(
    ${target}
    "${CMAKE_CURRENT_SOURCE_DIR}/solutions/${source}"
  )
  add_test(NAME ${target} COMMAND ${target})
endforeach()

# Multi-file project solutions: one target per project directory.
file(GLOB_RECURSE clings_project_solution_mains
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/solutions"
  "${CMAKE_CURRENT_SOURCE_DIR}/solutions/*/*/main.c"
)
foreach(main IN LISTS clings_project_solution_mains)
  get_filename_component(project_dir "${main}" DIRECTORY)
  file(GLOB project_sources
    "${CMAKE_CURRENT_SOURCE_DIR}/solutions/${project_dir}/*.c"
  )
  string(REPLACE "/" "_" target "solution_${project_dir}")
  clings_add_target(${target} ${project_sources})
  target_include_directories(
    ${target}
    PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/solutions/${project_dir}"
  )
  add_test(NAME ${target} COMMAND ${target})
endforeach()

# Exercises are intentionally excluded from the default build.  Build one with:
#   cmake --build build --target exercise_01_types_variables_01_integer_types
file(GLOB_RECURSE clings_exercise_sources
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/exercises"
  "${CMAKE_CURRENT_SOURCE_DIR}/exercises/*.c"
)
foreach(source IN LISTS clings_exercise_sources)
  string(REPLACE "/" "_" target "exercise_${source}")
  string(REPLACE ".c" "" target "${target}")
  add_executable(
    ${target}
    EXCLUDE_FROM_ALL
    "${CMAKE_CURRENT_SOURCE_DIR}/exercises/${source}"
  )
  target_link_libraries(${target} PRIVATE clings_harness Threads::Threads)
  if(UNIX)
    target_link_libraries(${target} PRIVATE m)
  endif()
endforeach()

# Multi-file project exercises.
file(GLOB_RECURSE clings_project_exercise_mains
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/exercises"
  "${CMAKE_CURRENT_SOURCE_DIR}/exercises/*/*/main.c"
)
foreach(main IN LISTS clings_project_exercise_mains)
  get_filename_component(project_dir "${main}" DIRECTORY)
  file(GLOB project_sources
    "${CMAKE_CURRENT_SOURCE_DIR}/exercises/${project_dir}/*.c"
  )
  string(REPLACE "/" "_" target "exercise_${project_dir}")
  add_executable(${target} EXCLUDE_FROM_ALL ${project_sources})
  target_include_directories(
    ${target}
    PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/exercises/${project_dir}"
  )
  target_link_libraries(${target} PRIVATE clings_harness Threads::Threads)
  if(UNIX)
    target_link_libraries(${target} PRIVATE m)
  endif()
endforeach()

add_custom_target(
  verify
  COMMAND
    "${Python3_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/clings" verify
  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
  COMMENT "Verifying every clings solution"
)
