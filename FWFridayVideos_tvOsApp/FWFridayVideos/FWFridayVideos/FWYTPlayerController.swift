//
//  FWYTPlayerController.swift
//  FWFridayVideos
//
//  Created by Yevgeniy Prokoshev on 09.02.16.
//  Copyright © 2016 EP. All rights reserved.
//

import UIKit
import AVFoundation
import AVKit
import TVMLKit
import XCDYouTubeKit


class FWYTPlayerController: AVPlayerViewController {
    //call this method once after setting up your appController.
    func createPlayYT( appController:TVApplicationController ){
        
        //allows us to access the javascript context
        appController.evaluateInJavaScriptContext({(evaluation: JSContext) -> Void in
            
            //this is the block that will be called when javascript calls playYTblock(videoIdentifier)
            let playYTblock : @convention(block) (String) -> Void = {
                (videoIdentifier : String) -> Void in
                
                print("Playing YouTube Video with ID:", videoIdentifier)
                
                let playerViewController = AVPlayerViewController()
                
                if var topController = UIApplication.sharedApplication().keyWindow?.rootViewController {
                    while let presentedViewController = topController.presentedViewController {
                        topController = presentedViewController
                    }
                    // topController should now be your topmost view controller
                    topController.presentViewController(playerViewController, animated: true, completion: nil)
                    
                    XCDYouTubeClient.defaultClient().getVideoWithIdentifier(videoIdentifier) { [weak playerViewController] (video: XCDYouTubeVideo?, error: NSError?) in
                        if let streamURL = (video?.streamURLs[XCDYouTubeVideoQualityHTTPLiveStreaming] ??
                            video?.streamURLs[XCDYouTubeVideoQuality.HD720.rawValue] ??
                            video?.streamURLs[XCDYouTubeVideoQuality.Medium360.rawValue] ??
                            video?.streamURLs[XCDYouTubeVideoQuality.Small240.rawValue]) {
                                playerViewController?.player = AVPlayer(URL: streamURL)
                                playerViewController?.player?.play()
                                playerViewController?.player?.actionAtItemEnd = AVPlayerActionAtItemEnd.None
                                
                                NSNotificationCenter.defaultCenter().addObserver(self, selector: "playerItemDidReachEnd:", name: AVPlayerItemDidPlayToEndTimeNotification, object: playerViewController?.player?.currentItem)
                                
                        } else {
                            self.dismissViewControllerAnimated(true, completion: nil)
                        }
                    }
                }
            }
            
            //this creates a function in the javascript context called "playYTblock".
            //calling playYTblock(videoIdentifier) in javascript will call the block we created above.
            evaluation.setObject(unsafeBitCast(playYTblock, AnyObject.self), forKeyedSubscript: "playYTblock")
            }, completion: {(Bool) -> Void in
                //evaluation block finished running
        })
    }
    
    func playerItemDidReachEnd(notification: NSNotification) {
        print("Video reached end! Dismiss player")
        
        if var topController = UIApplication.sharedApplication().keyWindow?.rootViewController {
            while let presentedViewController = topController.presentedViewController {
                topController = presentedViewController
            }
            // topController should now be your topmost view controller
            topController.dismissViewControllerAnimated(true, completion: nil)
        }
    }
}
