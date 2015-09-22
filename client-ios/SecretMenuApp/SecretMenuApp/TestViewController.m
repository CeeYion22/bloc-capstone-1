
//
//  TestViewController.m
//  SecretMenuApp
//
//  Created by Matthew Liu on 9/22/15.
//  Copyright (c) 2015 Unicycle Labs. All rights reserved.
//

#import "TestViewController.h"
#import "SMNDataSource.h"

@interface TestViewController ()

@end

@implementation TestViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    [[SMNDataSource sharedInstance] populateRestaurants];

}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
