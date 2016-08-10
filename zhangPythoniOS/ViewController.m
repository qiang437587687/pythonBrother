//
//  ViewController.m
//  tddddd
//
//  Created by zhang on 16/8/10.
//  Copyright © 2016年 zhang. All rights reserved.
//

#import "ViewController.h"
#include <Python/Python.h>
//#include <dlfcn.h>

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self zhangPython];
    
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)zhangPython {
    
    const char* main_script = [
                   [[NSBundle mainBundle] pathForResource:@"Library/Application Support/zhangPythonBundle.zhangpython/app/zhangpython/app"
                                                   ofType:@"py"] cStringUsingEncoding:NSUTF8StringEncoding];
    int ret;
    
    @try {
        FILE* fd = fopen(main_script, "r");
        if (fd == NULL) {
            ret = 1;
            NSLog(@"Unable to open file, abort.");
        } else {
            
            ret = PyRun_AnyFile(fd, main_script);
//            PyRun_String("print(\"nimei\")", <#s#>, <#g#>, <#l#>)
            
//            PyRun_AnyFile(<#fp#>, <#name#>)
            
            if (ret != 0) {
                NSLog(@"Application quit abnormally!");
            } else {
                NSLog(@"执行正确");
            }
        }
    }
    @catch (NSException *exception) {
        NSLog(@"Python runtime error: %@", [exception reason]);
    }
    
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
