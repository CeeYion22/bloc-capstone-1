//
//  SMNDataSource.h
//  SecretMenuApp
//
//  Created by Matthew Liu on 9/21/15.
//  Copyright (c) 2015 Unicycle Labs. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "SMNConstants.h"

@interface SMNDataSource : NSObject

@property (nonatomic, strong) NSMutableArray *restaurants;

+ (instancetype)sharedInstance;

- (void)populateRestaurants;

@end
