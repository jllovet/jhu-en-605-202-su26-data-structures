# Lab 2 TODO

## Implementation

- [x] Add comprehensive testing for whitespace
- [ ] Write docstring for clean
- [x] Use cleaner to write test for equivalence of cleaned and non-cleaned parsing
- [x] Model error propagation, with explicit plan for how errors should be routed, handled, or bubble up
- [x] Handle string with a single-pass
- [ ] Generator usage
- [ ] Add logger with flag for usage
- [ ] Add runtime metrics

## README

- [ ] Add description of allowed values, disallowing numbers for example
- [ ] Add usage information for flags, e.g. for logging


## Analysis

- [ ] Update strategy diagrams
- [ ] Add section What I Learned
  - [ ] Add note about how factoring error logging to the custom error classes themselves was not helpful, because it resulted in lost context
  - [ ] Add note about how writing this in an object-oriented/imperative style, even with recursion, made the structure of the core _pre2post function unwieldy. I would rather have wrapper functions. I don't like that in the way I've written the program, there are side effects liberally spread around the functions (e.g. writing to logs)
- [ ] Add section Enhancements

### Enhancements

- [ ] Add description of cleaner to write test for equivalence of cleaned and non-cleaned parsing
- [ ] Add note about unit testing
- [ ] Add note about unicode
