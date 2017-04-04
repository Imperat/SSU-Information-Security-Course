(deffunction ask-question (?question $?allowed-values)
    (printout t ?question)
    (bind ?answer (read))

    (if (lexemep ?answer) then
        (bind ?answer (lowcase ?answer)))

    (while (not (member ?answer ?allowed-values)) do
        (printout t ?question)
        (bind ?answer (read))

        (if (lexemep ?answer) then
            (bind ?answer (lowcase ?answer)))
    )

    ?answer
)

(deffunction yes-or-no-p (?question)
    (bind ?response (ask-question ?question yes no у n))
    (or (eq ?response yes) (eq ?response y))
)
