/** @param {NS} ns */
import { formatMoney } from 'utils/utils.js'
export async function main(ns) {

    const symbols = ns.stock.getSymbols()
    for (let sym of symbols) {


        if (ns.stock.getPosition(sym)[0] > 0) {
            const price = ns.stock.sellStock(sym, ns.stock.getPosition(sym)[0])
            ns.print("selling: " + sym)
            ns.write('stock-log.txt', `Sold: ${sym} at ${formatMoney(price)} [${ns.stock.getPosition(sym)[0]}]\n`, 'a')
        }
    }
}