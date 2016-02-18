//
//  AppDelegate.swift
//  FWFridayVideos
//
//  Created by Yevgeniy Prokoshev on 06.02.16.
//  Copyright © 2016 EP. All rights reserved.
//

import UIKit
import TVMLKit


@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, TVApplicationControllerDelegate {

    var window: UIWindow?
    let playerVC = FWYTPlayerController()
    var appController :TVApplicationController?
    
    static let TVBaseURL = "http://localhost:8080/"
    static let TVBootURL = "\(AppDelegate.TVBaseURL)static/javaScript/application.js"

    func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool
    {

        self.window = UIWindow(frame: UIScreen.mainScreen().bounds)


        let appControllerContext = TVApplicationControllerContext()
        appControllerContext.launchOptions["BASEURL"] = AppDelegate.TVBaseURL
        
        guard let javascriptURL = NSURL (string: AppDelegate.TVBootURL)  else { fatalError( "Error Creating URL") }
        
        
        appControllerContext.javaScriptApplicationURL = javascriptURL
        

        if let options = launchOptions {
            for (kind, value) in options {
                if let kindString = kind as? String {
                    appControllerContext.launchOptions[kindString] = value
                }
            }
        }
        
        self.appController = TVApplicationController(context: appControllerContext, window: self.window, delegate: self)
        playerVC.createPlayYT(self.appController!)

        return true
    }

}

