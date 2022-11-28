/** @param {NS} ns */
import {formatMoney} from 'utils.js' 
export async function main(ns) {

	ns.disableLog('ALL')
	ns.print("Starting...")

	const symbols = ns.stock.getSymbols()
	const minPurchase = ns.args.length >0 ? ns.args[0] * 1000000 : 10000000 //need to have atleast 10Million

	while (true) {
		var symbolRanking = []
		for (let sym of symbols) {
			const vol = ns.stock.getVolatility(sym)
			const forecast = ns.stock.getForecast(sym)
			const rank = (forecast - 0.5) * vol
			symbolRanking.push([sym, rank])

			if (forecast < 0.5 && ns.stock.getPosition(sym)[0] > 0) {
				const price = ns.stock.sellStock(sym, ns.stock.getPosition(sym)[0])
				ns.print("selling: " + sym)
				ns.write('stock-log.txt', `Sold: ${sym} at ${formatMoney(price)} [${ns.stock.getPosition(sym)[0]}]\n`, 'a')
			}
		}

		symbolRanking.sort((a, b) => b[1] - a[1])

		var purchasingPower = ns.getPlayer().money
		for (let rank of symbolRanking) {
			const [rSym, rRank] = rank
			if (rRank < 0 || purchasingPower < minPurchase) {
				break
			}
			let amount = Math.min(Math.floor(ns.getPlayer().money / (ns.stock.getAskPrice(rSym)*1.02)), ns.stock.getMaxShares(rSym)-ns.stock.getPosition(rSym)[0])
			let boughtAt = ns.stock.buyStock(rSym, amount)
			if (boughtAt != 0) {
				purchasingPower -= boughtAt * amount;
				ns.print(`Bought: ${rSym} at ${formatMoney(boughtAt)}`)
				ns.write('stock-log.txt', `Bought: ${rSym} at ${formatMoney(boughtAt)} [${amount}]\n`, 'a')
			} else {
				ns.print(`Couldn't buy ${rSym} with amount ${amount} current price is ${ns.stock.getAskPrice(rSym)}`)
			}

		}

		await ns.sleep(5000)
	}


}