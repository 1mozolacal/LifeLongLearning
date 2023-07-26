/** @param {NS} ns */
export async function main(ns) {


    if (!ns.stock.hasWSEAccount()) {
        const bought = ns.stock.purchaseWseAccount()
        if (!bought) {
            ns.alert("You need a WSE account, exiting stock bootloader...")
            ns.exit("you need a WSE Account")
        }
    }
    if (!ns.stock.hasTIXAPIAccess()) {
        const bought = ns.stock.purchaseTixApi()
        if (!bought) {
            ns.alert("You need TIX API, exiting stock bootloader...")
            ns.exit("you need TIX API")
        }
    }
    if (!ns.stock.has4SDataTIXAPI()) {
        const bought = ns.stock.purchase4SMarketDataTixApi()
        if (!bought) {
            ns.alert("You need 4S API, exiting stock bootloader...")
            ns.exit("you need 4S API")
        }
    }


}