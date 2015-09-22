//
//  SMNRestaurant.h
//  SecretMenuApp
//
//  Created by Matthew Liu on 9/21/15.
//  Copyright (c) 2015 Unicycle Labs. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface SMNRestaurant : NSObject

@property (nonatomic, strong) NSString *name;
@property (nonatomic, strong) NSString *descriptionText;
@property (nonatomic, strong) NSString *imageUrl;
@property (nonatomic, strong) NSArray *menuItems;


@end
