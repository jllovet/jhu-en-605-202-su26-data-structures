# Lab 2 TODO

## Implementation

- [x] Add comprehensive testing for whitespace
- [x] Write docstring for clean
- [x] Use cleaner to write test for equivalence of cleaned and non-cleaned parsing
- [x] Model error propagation, with explicit plan for how errors should be routed, handled, or bubble up
- [x] Handle string with a single-pass
- [x] Generator usage
- [x] Add logger
- [x] Add flag for logger usage
- [ ] Add runtime metrics

## README

- [x] Add description of allowed values, disallowing numbers for example
- [x] Add usage information for flags, e.g. for logging

## Analysis

- [x] Update strategy diagrams
- [x] Add section What I Learned
  - [x] Add note about how factoring error logging to the custom error classes themselves was not helpful, because it resulted in lost context
  - [x] Add note about how writing this in an object-oriented/imperative style, even with recursion, made the structure of the core _pre2post function unwieldy. I would rather have wrapper functions. I don't like that in the way I've written the program, there are side effects liberally spread around the functions (e.g. writing to logs)
- [x] Add section Enhancements


### Enhancements

- [x] Add note about unit testing
  - [x] Add description of cleaner.clean to write test for equivalence of cleaned and non-cleaned parsing
  - [x] Add note about unicode
- [x] Logging, cmd line flag for logging
- [x] Generator to traverse tree in post-order (and inspiration for generator usage from discussion in office hours)
- [x] Custom error types
