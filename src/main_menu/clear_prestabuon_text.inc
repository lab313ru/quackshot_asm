                move.l  #$54160003,(a5)
                moveq   #0,d1
                move.l  d1,(a6)
                jmp     fill_vram_16_words
; End of function clear_press_start_button_mapping
