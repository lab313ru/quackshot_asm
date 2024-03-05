                move.l  #$54160003,(a5)
                lea     press_start_button_mapping(pc),a1
                move.l  (a1)+,(a6)
                jmp     copy_words_16
; End of function show_press_start_button_mapping
