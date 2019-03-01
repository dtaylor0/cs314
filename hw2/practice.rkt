#lang racket

; *********************************************
; *  314 Principles of Programming Languages  *
; *  Spring 2019                              *
; *********************************************

(require "test-dictionary.rkt")

(define word '(a b c))

(define printWordByLetter
  (lambda (w)
    (if (list? w)
      (begin 
        (map display w)
        (display "\n"))
      (display "bad input\n"))))

(define printDictionary
  (lambda (dict)
    (if (list? dict)
      (map printWordByLetter dict)
      (display "error\n"))))

(printWordByLetter word)
(printDictionary dictionary)
