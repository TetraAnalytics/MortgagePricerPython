def calculate_single_mtge_cash(m):
    balance = m.balance
    note_rate = m.note_rate

    cdr = m.staticCDR
    cpr = m.staticCPR

    for i in range(0, m.amortization_term):
        m.cashflows[i].balance = balance
        m.cashflows[i].scheduled_interest = balance * (note_rate - m.servicing) / 12
        m.cashflows[i].scheduled_payment = m.scheduled_payment(balance, note_rate, m.amortization_term - i, 0)

        m.cashflows[i].scheduled_principal = m.cashflows[i].scheduled_payment - balance * note_rate / 12
        balance -= m.cashflows[i].scheduled_principal

        m.cashflows[i].default_principal = m.default(balance, cdr)
        if m.LTV == 0:
            m.cashflows[i].default_loss = 0
        else:
            m.cashflows[i].default_loss = m.cashflows[i].default_principal * m.staticSeverity
        balance -= m.cashflows[i].default_principal

        if i == m.balloon_term:
            m.cashflows[i].prepayment_principal = balance
        else:
            m.cashflows[i].prepayment_principal = m.prepayment(balance, cpr)
        balance -= m.cashflows[i].prepayment_principal

    return
